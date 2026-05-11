





import java.util.List;
import java.util.ArrayList;

public class xal_Xal  {

    private String anyAttribute;
    private String version;
    private String any;





    private xal_DocumentRoot xal_documentroot;




    private List<xal_AddressDetails> xal_addressdetailss;


    public xal_Xal(
        String anyAttribute,        String version,        String any    ) {
        this.anyAttribute = anyAttribute;
        this.version = version;
        this.any = any;
        this.xal_addressdetailss = new ArrayList<>();
    }

    public xal_Xal(
        String anyAttribute,        String version,        String any        ArrayList<xal_AddressDetails> xal_addressdetailss    ) {
        this.anyAttribute = anyAttribute;
        this.version = version;
        this.any = any;
        this.xal_addressdetailss = xal_addressdetailss;
    }

    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }

    public xal_DocumentRoot getXal_documentroot() {
        return xal_documentroot;
    }

    public void setXal_documentroot(xal_DocumentRoot xal_documentroot) {
        this.xal_documentroot = xal_documentroot;
    }
    public List<xal_AddressDetails> getXal_addressdetailss() {
        return xal_addressdetailss;
    }

    public void addXal_addressdetails(Xal_addressdetails xal_addressdetails) {
        this.xal_addressdetailss.add(xal_addressdetails);
    }

}