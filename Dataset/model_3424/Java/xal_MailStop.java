





import java.util.List;
import java.util.ArrayList;

public class xal_MailStop  {

    private String type;
    private String any;
    private String anyAttribute;





    private List<xal_AddressLine> xal_addresslines;




    private xal_SubPremise xal_subpremise;




    private xal_Department xal_department;


    public xal_MailStop(
        String type,        String any,        String anyAttribute    ) {
        this.type = type;
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.xal_addresslines = new ArrayList<>();
    }

    public xal_MailStop(
        String type,        String any,        String anyAttribute        ArrayList<xal_AddressLine> xal_addresslines    ) {
        this.type = type;
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

    public List<xal_AddressLine> getXal_addresslines() {
        return xal_addresslines;
    }

    public void addXal_addressline(Xal_addressline xal_addressline) {
        this.xal_addresslines.add(xal_addressline);
    }
    public xal_SubPremise getXal_subpremise() {
        return xal_subpremise;
    }

    public void setXal_subpremise(xal_SubPremise xal_subpremise) {
        this.xal_subpremise = xal_subpremise;
    }
    public xal_Department getXal_department() {
        return xal_department;
    }

    public void setXal_department(xal_Department xal_department) {
        this.xal_department = xal_department;
    }

}