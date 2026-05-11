





import java.util.List;
import java.util.ArrayList;

public class bpmn_SequenceEdge extends NamedBpmnObject, AssociationTarget {

    private String isDefault;
    private String conditionType;



    public bpmn_SequenceEdge(
        String isDefault,        String conditionType    ) {
        super(
        );
        this.isDefault = isDefault;
        this.conditionType = conditionType;
    }


    public String getIsdefault() {
        return isDefault;
    }

    public void setIsdefault(String isDefault) {
        this.isDefault = isDefault;
    }
    public String getConditiontype() {
        return conditionType;
    }

    public void setConditiontype(String conditionType) {
        this.conditionType = conditionType;
    }


}