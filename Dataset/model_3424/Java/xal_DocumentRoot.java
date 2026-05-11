





import java.util.List;
import java.util.ArrayList;

public class xal_DocumentRoot  {

    private String mixed;





    private List<xal_Locality> xal_localitys;




    private List<xal_EStringToStringMapEntry> xal_estringtostringmapentrys;




    private List<xal_Premise> xal_premises;




    private List<xal_AddressLine> xal_addresslines;




    private List<xal_AddressDetails> xal_addressdetailss;




    private List<xal_PostBox> xal_postboxs;




    private List<xal_PostalCode> xal_postalcodes;




    private List<xal_EStringToStringMapEntry> xal_estringtostringmapentrys;




    private List<xal_Department> xal_departments;




    private List<xal_Thoroughfare> xal_thoroughfares;




    private List<xal_CountryName> xal_countrynames;




    private List<xal_PostOffice> xal_postoffices;




    private List<xal_AdministrativeArea> xal_administrativeareas;


    public xal_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.xal_localitys = new ArrayList<>();
        this.xal_estringtostringmapentrys = new ArrayList<>();
        this.xal_premises = new ArrayList<>();
        this.xal_addresslines = new ArrayList<>();
        this.xal_addressdetailss = new ArrayList<>();
        this.xal_postboxs = new ArrayList<>();
        this.xal_postalcodes = new ArrayList<>();
        this.xal_estringtostringmapentrys = new ArrayList<>();
        this.xal_departments = new ArrayList<>();
        this.xal_thoroughfares = new ArrayList<>();
        this.xal_countrynames = new ArrayList<>();
        this.xal_postoffices = new ArrayList<>();
        this.xal_administrativeareas = new ArrayList<>();
    }

    public xal_DocumentRoot(
        String mixed        ArrayList<xal_Locality> xal_localitys,        ArrayList<xal_EStringToStringMapEntry> xal_estringtostringmapentrys,        ArrayList<xal_Premise> xal_premises,        ArrayList<xal_AddressLine> xal_addresslines,        ArrayList<xal_AddressDetails> xal_addressdetailss,        ArrayList<xal_PostBox> xal_postboxs,        ArrayList<xal_PostalCode> xal_postalcodes,        ArrayList<xal_EStringToStringMapEntry> xal_estringtostringmapentrys,        ArrayList<xal_Department> xal_departments,        ArrayList<xal_Thoroughfare> xal_thoroughfares,        ArrayList<xal_CountryName> xal_countrynames,        ArrayList<xal_PostOffice> xal_postoffices,        ArrayList<xal_AdministrativeArea> xal_administrativeareas    ) {
        this.mixed = mixed;
        this.xal_localitys = xal_localitys;
        this.xal_estringtostringmapentrys = xal_estringtostringmapentrys;
        this.xal_premises = xal_premises;
        this.xal_addresslines = xal_addresslines;
        this.xal_addressdetailss = xal_addressdetailss;
        this.xal_postboxs = xal_postboxs;
        this.xal_postalcodes = xal_postalcodes;
        this.xal_estringtostringmapentrys = xal_estringtostringmapentrys;
        this.xal_departments = xal_departments;
        this.xal_thoroughfares = xal_thoroughfares;
        this.xal_countrynames = xal_countrynames;
        this.xal_postoffices = xal_postoffices;
        this.xal_administrativeareas = xal_administrativeareas;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<xal_Locality> getXal_localitys() {
        return xal_localitys;
    }

    public void addXal_locality(Xal_locality xal_locality) {
        this.xal_localitys.add(xal_locality);
    }
    public List<xal_EStringToStringMapEntry> getXal_estringtostringmapentrys() {
        return xal_estringtostringmapentrys;
    }

    public void addXal_estringtostringmapentry(Xal_estringtostringmapentry xal_estringtostringmapentry) {
        this.xal_estringtostringmapentrys.add(xal_estringtostringmapentry);
    }
    public List<xal_Premise> getXal_premises() {
        return xal_premises;
    }

    public void addXal_premise(Xal_premise xal_premise) {
        this.xal_premises.add(xal_premise);
    }
    public List<xal_AddressLine> getXal_addresslines() {
        return xal_addresslines;
    }

    public void addXal_addressline(Xal_addressline xal_addressline) {
        this.xal_addresslines.add(xal_addressline);
    }
    public List<xal_AddressDetails> getXal_addressdetailss() {
        return xal_addressdetailss;
    }

    public void addXal_addressdetails(Xal_addressdetails xal_addressdetails) {
        this.xal_addressdetailss.add(xal_addressdetails);
    }
    public List<xal_PostBox> getXal_postboxs() {
        return xal_postboxs;
    }

    public void addXal_postbox(Xal_postbox xal_postbox) {
        this.xal_postboxs.add(xal_postbox);
    }
    public List<xal_PostalCode> getXal_postalcodes() {
        return xal_postalcodes;
    }

    public void addXal_postalcode(Xal_postalcode xal_postalcode) {
        this.xal_postalcodes.add(xal_postalcode);
    }
    public List<xal_EStringToStringMapEntry> getXal_estringtostringmapentrys() {
        return xal_estringtostringmapentrys;
    }

    public void addXal_estringtostringmapentry(Xal_estringtostringmapentry xal_estringtostringmapentry) {
        this.xal_estringtostringmapentrys.add(xal_estringtostringmapentry);
    }
    public List<xal_Department> getXal_departments() {
        return xal_departments;
    }

    public void addXal_department(Xal_department xal_department) {
        this.xal_departments.add(xal_department);
    }
    public List<xal_Thoroughfare> getXal_thoroughfares() {
        return xal_thoroughfares;
    }

    public void addXal_thoroughfare(Xal_thoroughfare xal_thoroughfare) {
        this.xal_thoroughfares.add(xal_thoroughfare);
    }
    public List<xal_CountryName> getXal_countrynames() {
        return xal_countrynames;
    }

    public void addXal_countryname(Xal_countryname xal_countryname) {
        this.xal_countrynames.add(xal_countryname);
    }
    public List<xal_PostOffice> getXal_postoffices() {
        return xal_postoffices;
    }

    public void addXal_postoffice(Xal_postoffice xal_postoffice) {
        this.xal_postoffices.add(xal_postoffice);
    }
    public List<xal_AdministrativeArea> getXal_administrativeareas() {
        return xal_administrativeareas;
    }

    public void addXal_administrativearea(Xal_administrativearea xal_administrativearea) {
        this.xal_administrativeareas.add(xal_administrativearea);
    }

}