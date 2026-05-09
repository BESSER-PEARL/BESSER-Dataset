





import java.util.List;
import java.util.ArrayList;

public class uma_MethodUnit extends MethodElement {

    private String authors;
    private String version;
    private String changeDescription;
    private String changeDate;



    public uma_MethodUnit(
        String authors,        String version,        String changeDescription,        String changeDate    ) {
        super(
        );
        this.authors = authors;
        this.version = version;
        this.changeDescription = changeDescription;
        this.changeDate = changeDate;
    }


    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getChangedescription() {
        return changeDescription;
    }

    public void setChangedescription(String changeDescription) {
        this.changeDescription = changeDescription;
    }
    public String getChangedate() {
        return changeDate;
    }

    public void setChangedate(String changeDate) {
        this.changeDate = changeDate;
    }


}