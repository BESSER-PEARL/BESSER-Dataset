





import java.util.List;
import java.util.ArrayList;

public class core_ModelElementReference extends IdentifiedElement {

    private String reason;
    private String weight;
    private String satisfactionLevel;
    private String verifies;



    public core_ModelElementReference(
        String reason,        String weight,        String satisfactionLevel,        String verifies    ) {
        super(
        );
        this.reason = reason;
        this.weight = weight;
        this.satisfactionLevel = satisfactionLevel;
        this.verifies = verifies;
    }


    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
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


}