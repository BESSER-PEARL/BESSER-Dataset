





import java.util.List;
import java.util.ArrayList;

public class uma_MethodUnit extends MethodElement {

    private String changeDescription;
    private String copyright;
    private String authors;
    private String changeDate;
    private String version;



    public uma_MethodUnit(
        String changeDescription,        String copyright,        String authors,        String changeDate,        String version    ) {
        super(
        );
        this.changeDescription = changeDescription;
        this.copyright = copyright;
        this.authors = authors;
        this.changeDate = changeDate;
        this.version = version;
    }


    public String getChangedescription() {
        return changeDescription;
    }

    public void setChangedescription(String changeDescription) {
        this.changeDescription = changeDescription;
    }
    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }
    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }
    public String getChangedate() {
        return changeDate;
    }

    public void setChangedate(String changeDate) {
        this.changeDate = changeDate;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}