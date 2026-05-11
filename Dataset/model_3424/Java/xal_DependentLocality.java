





import java.util.List;
import java.util.ArrayList;

public class xal_DependentLocality  {

    private String anyAttribute;
    private String usageType;
    private String any;
    private String type;
    private String indicator;
    private String connector;





    private xal_Thoroughfare xal_thoroughfare;




    private xal_PostOffice xal_postoffice;




    private xal_Locality xal_locality;




    private xal_PostalCode xal_postalcode;




    private xal_Thoroughfare xal_thoroughfare;




    private List<xal_AddressLine> xal_addresslines;




    private xal_DependentLocality xal_dependentlocality;


    public xal_DependentLocality(
        String anyAttribute,        String usageType,        String any,        String type,        String indicator,        String connector    ) {
        this.anyAttribute = anyAttribute;
        this.usageType = usageType;
        this.any = any;
        this.type = type;
        this.indicator = indicator;
        this.connector = connector;
        this.xal_addresslines = new ArrayList<>();
    }

    public xal_DependentLocality(
        String anyAttribute,        String usageType,        String any,        String type,        String indicator,        String connector        ArrayList<xal_AddressLine> xal_addresslines    ) {
        this.anyAttribute = anyAttribute;
        this.usageType = usageType;
        this.any = any;
        this.type = type;
        this.indicator = indicator;
        this.connector = connector;
        this.xal_addresslines = xal_addresslines;
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
    public String getConnector() {
        return connector;
    }

    public void setConnector(String connector) {
        this.connector = connector;
    }

    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
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
    public xal_PostalCode getXal_postalcode() {
        return xal_postalcode;
    }

    public void setXal_postalcode(xal_PostalCode xal_postalcode) {
        this.xal_postalcode = xal_postalcode;
    }
    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
    }
    public List<xal_AddressLine> getXal_addresslines() {
        return xal_addresslines;
    }

    public void addXal_addressline(Xal_addressline xal_addressline) {
        this.xal_addresslines.add(xal_addressline);
    }
    public xal_DependentLocality getXal_dependentlocality() {
        return xal_dependentlocality;
    }

    public void setXal_dependentlocality(xal_DependentLocality xal_dependentlocality) {
        this.xal_dependentlocality = xal_dependentlocality;
    }

}