





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNActivity extends FlowNode {

    private String isForCompensation;
    private String completionQuantity;
    private String startQuantity;





    private BPMNProfile_CompensateEventDefinition bpmnprofile_compensateeventdefinition;


    public BPMNProfile_BPMNActivity(
        String isForCompensation,        String completionQuantity,        String startQuantity    ) {
        super(
        );
        this.isForCompensation = isForCompensation;
        this.completionQuantity = completionQuantity;
        this.startQuantity = startQuantity;
    }


    public String getIsforcompensation() {
        return isForCompensation;
    }

    public void setIsforcompensation(String isForCompensation) {
        this.isForCompensation = isForCompensation;
    }
    public String getCompletionquantity() {
        return completionQuantity;
    }

    public void setCompletionquantity(String completionQuantity) {
        this.completionQuantity = completionQuantity;
    }
    public String getStartquantity() {
        return startQuantity;
    }

    public void setStartquantity(String startQuantity) {
        this.startQuantity = startQuantity;
    }

    public BPMNProfile_CompensateEventDefinition getBpmnprofile_compensateeventdefinition() {
        return bpmnprofile_compensateeventdefinition;
    }

    public void setBpmnprofile_compensateeventdefinition(BPMNProfile_CompensateEventDefinition bpmnprofile_compensateeventdefinition) {
        this.bpmnprofile_compensateeventdefinition = bpmnprofile_compensateeventdefinition;
    }

}