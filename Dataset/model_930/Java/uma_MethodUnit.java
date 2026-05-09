





import java.util.List;
import java.util.ArrayList;

public class uma_MethodUnit extends MethodElement {

    private String authors;
    private String changeDescription;
    private String version;
    private String changeDate;





    private uma_SupportingMaterial uma_supportingmaterial;


    public uma_MethodUnit(
        String authors,        String changeDescription,        String version,        String changeDate    ) {
        super(
        );
        this.authors = authors;
        this.changeDescription = changeDescription;
        this.version = version;
        this.changeDate = changeDate;
    }


    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }
    public String getChangedescription() {
        return changeDescription;
    }

    public void setChangedescription(String changeDescription) {
        this.changeDescription = changeDescription;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getChangedate() {
        return changeDate;
    }

    public void setChangedate(String changeDate) {
        this.changeDate = changeDate;
    }

    public uma_SupportingMaterial getUma_supportingmaterial() {
        return uma_supportingmaterial;
    }

    public void setUma_supportingmaterial(uma_SupportingMaterial uma_supportingmaterial) {
        this.uma_supportingmaterial = uma_supportingmaterial;
    }

}