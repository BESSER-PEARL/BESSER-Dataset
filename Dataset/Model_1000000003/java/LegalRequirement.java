





import java.util.List;
import java.util.ArrayList;

public class LegalRequirement  {

    private String standard;
    private String principle;
    private String legal_ref;





    private Project project;


    public LegalRequirement(
        String standard,        String principle,        String legal_ref    ) {
        this.standard = standard;
        this.principle = principle;
        this.legal_ref = legal_ref;
    }


    public String getStandard() {
        return standard;
    }

    public void setStandard(String standard) {
        this.standard = standard;
    }
    public String getPrinciple() {
        return principle;
    }

    public void setPrinciple(String principle) {
        this.principle = principle;
    }
    public String getLegal_ref() {
        return legal_ref;
    }

    public void setLegal_ref(String legal_ref) {
        this.legal_ref = legal_ref;
    }

    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }

}