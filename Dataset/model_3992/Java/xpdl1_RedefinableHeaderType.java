





import java.util.List;
import java.util.ArrayList;

public class xpdl1_RedefinableHeaderType  {

    private String codepage;
    private String publicationStatus;
    private String countrykey;
    private String author;
    private String version;





    private xpdl1_PackageType xpdl1_packagetype;




    private xpdl1_DocumentRoot xpdl1_documentroot;


    public xpdl1_RedefinableHeaderType(
        String codepage,        String publicationStatus,        String countrykey,        String author,        String version    ) {
        this.codepage = codepage;
        this.publicationStatus = publicationStatus;
        this.countrykey = countrykey;
        this.author = author;
        this.version = version;
    }


    public String getCodepage() {
        return codepage;
    }

    public void setCodepage(String codepage) {
        this.codepage = codepage;
    }
    public String getPublicationstatus() {
        return publicationStatus;
    }

    public void setPublicationstatus(String publicationStatus) {
        this.publicationStatus = publicationStatus;
    }
    public String getCountrykey() {
        return countrykey;
    }

    public void setCountrykey(String countrykey) {
        this.countrykey = countrykey;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public xpdl1_PackageType getXpdl1_packagetype() {
        return xpdl1_packagetype;
    }

    public void setXpdl1_packagetype(xpdl1_PackageType xpdl1_packagetype) {
        this.xpdl1_packagetype = xpdl1_packagetype;
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }

}