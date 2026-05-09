





import java.util.List;
import java.util.ArrayList;

public class doc_builder_BookBuilder extends Map {

    private String version;
    private String title;
    private String license;
    private String copyrightMarker;





    private List<builder_PropertyEntry> builder_propertyentrys;




    private List<Author> authors;




    private List<Copyright> copyrights;


    public doc_builder_BookBuilder(
        String version,        String title,        String license,        String copyrightMarker    ) {
        super(
        );
        this.version = version;
        this.title = title;
        this.license = license;
        this.copyrightMarker = copyrightMarker;
        this.builder_propertyentrys = new ArrayList<>();
        this.authors = new ArrayList<>();
        this.copyrights = new ArrayList<>();
    }

    public doc_builder_BookBuilder(
        String version,        String title,        String license,        String copyrightMarker        ArrayList<builder_PropertyEntry> builder_propertyentrys,        ArrayList<Author> authors,        ArrayList<Copyright> copyrights    ) {
        this.version = version;
        this.title = title;
        this.license = license;
        this.copyrightMarker = copyrightMarker;
        this.builder_propertyentrys = builder_propertyentrys;
        this.authors = authors;
        this.copyrights = copyrights;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }
    public String getCopyrightmarker() {
        return copyrightMarker;
    }

    public void setCopyrightmarker(String copyrightMarker) {
        this.copyrightMarker = copyrightMarker;
    }

    public List<builder_PropertyEntry> getBuilder_propertyentrys() {
        return builder_propertyentrys;
    }

    public void addBuilder_propertyentry(Builder_propertyentry builder_propertyentry) {
        this.builder_propertyentrys.add(builder_propertyentry);
    }
    public List<Author> getAuthors() {
        return authors;
    }

    public void addAuthor(Author author) {
        this.authors.add(author);
    }
    public List<Copyright> getCopyrights() {
        return copyrights;
    }

    public void addCopyright(Copyright copyright) {
        this.copyrights.add(copyright);
    }

}