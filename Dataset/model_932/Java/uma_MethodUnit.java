





import java.util.List;
import java.util.ArrayList;

public class uma_MethodUnit extends MethodElement {

    private String version;
    private String authors;
    private String changeDate;
    private String changeDescription;



    public uma_MethodUnit(
        String version,        String authors,        String changeDate,        String changeDescription    ) {
        super(
        );
        this.version = version;
        this.authors = authors;
        this.changeDate = changeDate;
        this.changeDescription = changeDescription;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
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
    public String getChangedescription() {
        return changeDescription;
    }

    public void setChangedescription(String changeDescription) {
        this.changeDescription = changeDescription;
    }


}