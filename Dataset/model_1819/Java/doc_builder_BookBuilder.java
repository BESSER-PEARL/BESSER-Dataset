





import java.util.List;
import java.util.ArrayList;

public class doc_builder_BookBuilder extends Map {

    private String title;
    private String copyrightMarker;
    private String license;
    private String version;





    private List<Copyright> copyrights;


    public doc_builder_BookBuilder(
        String title,        String copyrightMarker,        String license,        String version    ) {
        super(
        );
        this.title = title;
        this.copyrightMarker = copyrightMarker;
        this.license = license;
        this.version = version;
        this.copyrights = new ArrayList<>();
    }

    public doc_builder_BookBuilder(
        String title,        String copyrightMarker,        String license,        String version        ArrayList<Copyright> copyrights    ) {
        this.title = title;
        this.copyrightMarker = copyrightMarker;
        this.license = license;
        this.version = version;
        this.copyrights = copyrights;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getCopyrightmarker() {
        return copyrightMarker;
    }

    public void setCopyrightmarker(String copyrightMarker) {
        this.copyrightMarker = copyrightMarker;
    }
    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public List<Copyright> getCopyrights() {
        return copyrights;
    }

    public void addCopyright(Copyright copyright) {
        this.copyrights.add(copyright);
    }

}