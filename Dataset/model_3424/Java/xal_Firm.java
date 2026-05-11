





import java.util.List;
import java.util.ArrayList;

public class xal_Firm  {

    private String any;
    private String type;
    private String anyAttribute;





    private xal_Premise xal_premise;




    private xal_Thoroughfare xal_thoroughfare;




    private xal_SubPremise xal_subpremise;




    private xal_PostBox xal_postbox;




    private List<xal_Department> xal_departments;




    private xal_MailStop xal_mailstop;




    private List<xal_AddressLine> xal_addresslines;




    private xal_PostalCode xal_postalcode;


    public xal_Firm(
        String any,        String type,        String anyAttribute    ) {
        this.any = any;
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.xal_departments = new ArrayList<>();
        this.xal_addresslines = new ArrayList<>();
    }

    public xal_Firm(
        String any,        String type,        String anyAttribute        ArrayList<xal_Department> xal_departments,        ArrayList<xal_AddressLine> xal_addresslines    ) {
        this.any = any;
        this.type = type;
        this.anyAttribute = anyAttribute;
        this.xal_departments = xal_departments;
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

    public xal_Premise getXal_premise() {
        return xal_premise;
    }

    public void setXal_premise(xal_Premise xal_premise) {
        this.xal_premise = xal_premise;
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
    public xal_PostBox getXal_postbox() {
        return xal_postbox;
    }

    public void setXal_postbox(xal_PostBox xal_postbox) {
        this.xal_postbox = xal_postbox;
    }
    public List<xal_Department> getXal_departments() {
        return xal_departments;
    }

    public void addXal_department(Xal_department xal_department) {
        this.xal_departments.add(xal_department);
    }
    public xal_MailStop getXal_mailstop() {
        return xal_mailstop;
    }

    public void setXal_mailstop(xal_MailStop xal_mailstop) {
        this.xal_mailstop = xal_mailstop;
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