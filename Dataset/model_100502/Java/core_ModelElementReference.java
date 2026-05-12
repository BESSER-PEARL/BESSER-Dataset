





import java.util.List;
import java.util.ArrayList;

public class core_ModelElementReference extends IdentifiedElement {

    private String satisfactionLevel;
    private String verifies;
    private String weight;
    private String reason;





    private core_EObject core_eobject;


    public core_ModelElementReference(
        String satisfactionLevel,        String verifies,        String weight,        String reason    ) {
        super(
        );
        this.satisfactionLevel = satisfactionLevel;
        this.verifies = verifies;
        this.weight = weight;
        this.reason = reason;
    }


    public String getSatisfactionlevel() {
        return satisfactionLevel;
    }

    public void setSatisfactionlevel(String satisfactionLevel) {
        this.satisfactionLevel = satisfactionLevel;
    }
    public String getVerifies() {
        return verifies;
    }

    public void setVerifies(String verifies) {
        this.verifies = verifies;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }

    public core_EObject getCore_eobject() {
        return core_eobject;
    }

    public void setCore_eobject(core_EObject core_eobject) {
        this.core_eobject = core_eobject;
    }

}