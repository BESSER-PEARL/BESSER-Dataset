





import java.util.List;
import java.util.ArrayList;

public class umm_TC_Constraint  {

    private String listIdentifier;
    private String responsibleAgency;
    private String kind;





    private umm_Constraint umm_constraint;


    public umm_TC_Constraint(
        String listIdentifier,        String responsibleAgency,        String kind    ) {
        this.listIdentifier = listIdentifier;
        this.responsibleAgency = responsibleAgency;
        this.kind = kind;
    }


    public String getListidentifier() {
        return listIdentifier;
    }

    public void setListidentifier(String listIdentifier) {
        this.listIdentifier = listIdentifier;
    }
    public String getResponsibleagency() {
        return responsibleAgency;
    }

    public void setResponsibleagency(String responsibleAgency) {
        this.responsibleAgency = responsibleAgency;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public umm_Constraint getUmm_constraint() {
        return umm_constraint;
    }

    public void setUmm_constraint(umm_Constraint umm_constraint) {
        this.umm_constraint = umm_constraint;
    }

}