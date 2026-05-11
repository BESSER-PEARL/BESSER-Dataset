





import java.util.List;
import java.util.ArrayList;

public class core_ModelElementReference extends IdentifiedElement {

    private String verifies;
    private String reason;
    private String satisfactionLevel;
    private String weight;





    private core_ReferencedModelElements core_referencedmodelelements;




    private core_ReferencedModelElements core_referencedmodelelements;


    public core_ModelElementReference(
        String verifies,        String reason,        String satisfactionLevel,        String weight    ) {
        super(
        );
        this.verifies = verifies;
        this.reason = reason;
        this.satisfactionLevel = satisfactionLevel;
        this.weight = weight;
    }


    public String getVerifies() {
        return verifies;
    }

    public void setVerifies(String verifies) {
        this.verifies = verifies;
    }
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }
    public String getSatisfactionlevel() {
        return satisfactionLevel;
    }

    public void setSatisfactionlevel(String satisfactionLevel) {
        this.satisfactionLevel = satisfactionLevel;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }

    public core_ReferencedModelElements getCore_referencedmodelelements() {
        return core_referencedmodelelements;
    }

    public void setCore_referencedmodelelements(core_ReferencedModelElements core_referencedmodelelements) {
        this.core_referencedmodelelements = core_referencedmodelelements;
    }
    public core_ReferencedModelElements getCore_referencedmodelelements() {
        return core_referencedmodelelements;
    }

    public void setCore_referencedmodelelements(core_ReferencedModelElements core_referencedmodelelements) {
        this.core_referencedmodelelements = core_referencedmodelelements;
    }

}