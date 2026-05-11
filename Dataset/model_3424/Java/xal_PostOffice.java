





import java.util.List;
import java.util.ArrayList;

public class xal_PostOffice  {

    private String anyAttribute;
    private String any;
    private String type;
    private String indicator;





    private xal_PostOfficeNumber xal_postofficenumber;




    private List<xal_AddressLine> xal_addresslines;




    private xal_AdministrativeArea xal_administrativearea;




    private xal_SubAdministrativeArea xal_subadministrativearea;




    private List<xal_PostOfficeName> xal_postofficenames;




    private xal_Locality xal_locality;


    public xal_PostOffice(
        String anyAttribute,        String any,        String type,        String indicator    ) {
        this.anyAttribute = anyAttribute;
        this.any = any;
        this.type = type;
        this.indicator = indicator;
        this.xal_addresslines = new ArrayList<>();
        this.xal_postofficenames = new ArrayList<>();
    }

    public xal_PostOffice(
        String anyAttribute,        String any,        String type,        String indicator        ArrayList<xal_AddressLine> xal_addresslines,        ArrayList<xal_PostOfficeName> xal_postofficenames    ) {
        this.anyAttribute = anyAttribute;
        this.any = any;
        this.type = type;
        this.indicator = indicator;
        this.xal_addresslines = xal_addresslines;
        this.xal_postofficenames = xal_postofficenames;
    }

    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
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

    public xal_PostOfficeNumber getXal_postofficenumber() {
        return xal_postofficenumber;
    }

    public void setXal_postofficenumber(xal_PostOfficeNumber xal_postofficenumber) {
        this.xal_postofficenumber = xal_postofficenumber;
    }
    public List<xal_AddressLine> getXal_addresslines() {
        return xal_addresslines;
    }

    public void addXal_addressline(Xal_addressline xal_addressline) {
        this.xal_addresslines.add(xal_addressline);
    }
    public xal_AdministrativeArea getXal_administrativearea() {
        return xal_administrativearea;
    }

    public void setXal_administrativearea(xal_AdministrativeArea xal_administrativearea) {
        this.xal_administrativearea = xal_administrativearea;
    }
    public xal_SubAdministrativeArea getXal_subadministrativearea() {
        return xal_subadministrativearea;
    }

    public void setXal_subadministrativearea(xal_SubAdministrativeArea xal_subadministrativearea) {
        this.xal_subadministrativearea = xal_subadministrativearea;
    }
    public List<xal_PostOfficeName> getXal_postofficenames() {
        return xal_postofficenames;
    }

    public void addXal_postofficename(Xal_postofficename xal_postofficename) {
        this.xal_postofficenames.add(xal_postofficename);
    }
    public xal_Locality getXal_locality() {
        return xal_locality;
    }

    public void setXal_locality(xal_Locality xal_locality) {
        this.xal_locality = xal_locality;
    }

}