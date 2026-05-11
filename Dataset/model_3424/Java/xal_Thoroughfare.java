





import java.util.List;
import java.util.ArrayList;

public class xal_Thoroughfare  {

    private String dependentThoroughfaresConnector;
    private String group;
    private String any;
    private String dependentThoroughfaresType;
    private String anyAttribute;
    private String dependentThoroughfares;
    private String dependentThoroughfaresIndicator;
    private String type;





    private xal_Country xal_country;




    private List<xal_ThoroughfareNumberRange> xal_thoroughfarenumberranges;




    private xal_Locality xal_locality;




    private xal_AddressDetails xal_addressdetails;


    public xal_Thoroughfare(
        String dependentThoroughfaresConnector,        String group,        String any,        String dependentThoroughfaresType,        String anyAttribute,        String dependentThoroughfares,        String dependentThoroughfaresIndicator,        String type    ) {
        this.dependentThoroughfaresConnector = dependentThoroughfaresConnector;
        this.group = group;
        this.any = any;
        this.dependentThoroughfaresType = dependentThoroughfaresType;
        this.anyAttribute = anyAttribute;
        this.dependentThoroughfares = dependentThoroughfares;
        this.dependentThoroughfaresIndicator = dependentThoroughfaresIndicator;
        this.type = type;
        this.xal_thoroughfarenumberranges = new ArrayList<>();
    }

    public xal_Thoroughfare(
        String dependentThoroughfaresConnector,        String group,        String any,        String dependentThoroughfaresType,        String anyAttribute,        String dependentThoroughfares,        String dependentThoroughfaresIndicator,        String type        ArrayList<xal_ThoroughfareNumberRange> xal_thoroughfarenumberranges    ) {
        this.dependentThoroughfaresConnector = dependentThoroughfaresConnector;
        this.group = group;
        this.any = any;
        this.dependentThoroughfaresType = dependentThoroughfaresType;
        this.anyAttribute = anyAttribute;
        this.dependentThoroughfares = dependentThoroughfares;
        this.dependentThoroughfaresIndicator = dependentThoroughfaresIndicator;
        this.type = type;
        this.xal_thoroughfarenumberranges = xal_thoroughfarenumberranges;
    }

    public String getDependentthoroughfaresconnector() {
        return dependentThoroughfaresConnector;
    }

    public void setDependentthoroughfaresconnector(String dependentThoroughfaresConnector) {
        this.dependentThoroughfaresConnector = dependentThoroughfaresConnector;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getDependentthoroughfarestype() {
        return dependentThoroughfaresType;
    }

    public void setDependentthoroughfarestype(String dependentThoroughfaresType) {
        this.dependentThoroughfaresType = dependentThoroughfaresType;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getDependentthoroughfares() {
        return dependentThoroughfares;
    }

    public void setDependentthoroughfares(String dependentThoroughfares) {
        this.dependentThoroughfares = dependentThoroughfares;
    }
    public String getDependentthoroughfaresindicator() {
        return dependentThoroughfaresIndicator;
    }

    public void setDependentthoroughfaresindicator(String dependentThoroughfaresIndicator) {
        this.dependentThoroughfaresIndicator = dependentThoroughfaresIndicator;
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
    public List<xal_ThoroughfareNumberRange> getXal_thoroughfarenumberranges() {
        return xal_thoroughfarenumberranges;
    }

    public void addXal_thoroughfarenumberrange(Xal_thoroughfarenumberrange xal_thoroughfarenumberrange) {
        this.xal_thoroughfarenumberranges.add(xal_thoroughfarenumberrange);
    }
    public xal_Locality getXal_locality() {
        return xal_locality;
    }

    public void setXal_locality(xal_Locality xal_locality) {
        this.xal_locality = xal_locality;
    }
    public xal_AddressDetails getXal_addressdetails() {
        return xal_addressdetails;
    }

    public void setXal_addressdetails(xal_AddressDetails xal_addressdetails) {
        this.xal_addressdetails = xal_addressdetails;
    }

}