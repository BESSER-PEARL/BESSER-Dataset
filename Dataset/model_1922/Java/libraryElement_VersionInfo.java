





import java.util.List;
import java.util.ArrayList;

public class libraryElement_VersionInfo  {

    private String date;
    private String author;
    private String remarks;
    private String version;
    private String organization;





    private libraryElement_LibraryElement libraryelement_libraryelement;


    public libraryElement_VersionInfo(
        String date,        String author,        String remarks,        String version,        String organization    ) {
        this.date = date;
        this.author = author;
        this.remarks = remarks;
        this.version = version;
        this.organization = organization;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getRemarks() {
        return remarks;
    }

    public void setRemarks(String remarks) {
        this.remarks = remarks;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }

    public libraryElement_LibraryElement getLibraryelement_libraryelement() {
        return libraryelement_libraryelement;
    }

    public void setLibraryelement_libraryelement(libraryElement_LibraryElement libraryelement_libraryelement) {
        this.libraryelement_libraryelement = libraryelement_libraryelement;
    }

}