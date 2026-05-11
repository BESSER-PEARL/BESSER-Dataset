





import java.util.List;
import java.util.ArrayList;

public class eJSL_Manifestation  {

    private String link;
    private String version;
    private String creationdate;
    private String license;
    private String description;
    private String copyright;





    private eJSL_Extension ejsl_extension;


    public eJSL_Manifestation(
        String link,        String version,        String creationdate,        String license,        String description,        String copyright    ) {
        this.link = link;
        this.version = version;
        this.creationdate = creationdate;
        this.license = license;
        this.description = description;
        this.copyright = copyright;
    }


    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getCreationdate() {
        return creationdate;
    }

    public void setCreationdate(String creationdate) {
        this.creationdate = creationdate;
    }
    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }

    public eJSL_Extension getEjsl_extension() {
        return ejsl_extension;
    }

    public void setEjsl_extension(eJSL_Extension ejsl_extension) {
        this.ejsl_extension = ejsl_extension;
    }

}