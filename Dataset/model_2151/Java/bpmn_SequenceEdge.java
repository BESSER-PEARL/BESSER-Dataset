





import java.util.List;
import java.util.ArrayList;

public class bpmn_SequenceEdge extends Identifiable, NamedBpmnObject {

    private String conditionType;
    private String isDefault;



    public bpmn_SequenceEdge(
        String conditionType,        String isDefault    ) {
        super(
        );
        this.conditionType = conditionType;
        this.isDefault = isDefault;
    }


    public String getConditiontype() {
        return conditionType;
    }

    public void setConditiontype(String conditionType) {
        this.conditionType = conditionType;
    }
    public String getIsdefault() {
        return isDefault;
    }

    public void setIsdefault(String isDefault) {
        this.isDefault = isDefault;
    }


}