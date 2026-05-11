





import java.util.List;
import java.util.ArrayList;

public class xal_PostalCode  {

    private String any;
    private String type;
    private String anyAttribute;





    private List<xal_AddressLine> xal_addresslines;




    private xal_SubAdministrativeArea xal_subadministrativearea;




    private xal_AdministrativeArea xal_administrativearea;




    private xal_Locality xal_locality;




    private xal_Thoroughfare xal_thoroughfare;




    private xal_SubPremise xal_subpremise;




    private xal_PostOffice xal_postoffice;


    public xal_PostalCode(
        String any,        String type,        String anyAttribute    ) {
        this.any = any;
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.xal_addresslines = new ArrayList<>();
    }

    public xal_PostalCode(
        String any,        String type,        String anyAttribute        ArrayList<xal_AddressLine> xal_addresslines    ) {
        this.any = any;
        this.type = type;
        this.anyAttribute = anyAttribute;
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

    public List<xal_AddressLine> getXal_addresslines() {
        return xal_addresslines;
    }

    public void addXal_addressline(Xal_addressline xal_addressline) {
        this.xal_addresslines.add(xal_addressline);
    }
    public xal_SubAdministrativeArea getXal_subadministrativearea() {
        return xal_subadministrativearea;
    }

    public void setXal_subadministrativearea(xal_SubAdministrativeArea xal_subadministrativearea) {
        this.xal_subadministrativearea = xal_subadministrativearea;
    }
    public xal_AdministrativeArea getXal_administrativearea() {
        return xal_administrativearea;
    }

    public void setXal_administrativearea(xal_AdministrativeArea xal_administrativearea) {
        this.xal_administrativearea = xal_administrativearea;
    }
    public xal_Locality getXal_locality() {
        return xal_locality;
    }

    public void setXal_locality(xal_Locality xal_locality) {
        this.xal_locality = xal_locality;
    }
    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
    }
    public xal_SubPremise getXal_subpremise() {
        return xal_subpremise;
    }

    public void setXal_subpremise(xal_SubPremise xal_subpremise) {
        this.xal_subpremise = xal_subpremise;
    }
    public xal_PostOffice getXal_postoffice() {
        return xal_postoffice;
    }

    public void setXal_postoffice(xal_PostOffice xal_postoffice) {
        this.xal_postoffice = xal_postoffice;
    }

}