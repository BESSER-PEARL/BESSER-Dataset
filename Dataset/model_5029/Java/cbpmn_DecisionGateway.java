





import java.util.List;
import java.util.ArrayList;

public class cbpmn_DecisionGateway extends SplitGateway {

    private String type;





    private List<cbpmn_DecisionCondition> cbpmn_decisionconditions;


    public cbpmn_DecisionGateway(
        String type    ) {
        super(
        );
        this.type = type;
        this.cbpmn_decisionconditions = new ArrayList<>();
    }

    public cbpmn_DecisionGateway(
        String type        ArrayList<cbpmn_DecisionCondition> cbpmn_decisionconditions    ) {
        this.type = type;
        this.cbpmn_decisionconditions = cbpmn_decisionconditions;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<cbpmn_DecisionCondition> getCbpmn_decisionconditions() {
        return cbpmn_decisionconditions;
    }

    public void addCbpmn_decisioncondition(Cbpmn_decisioncondition cbpmn_decisioncondition) {
        this.cbpmn_decisionconditions.add(cbpmn_decisioncondition);
    }

}