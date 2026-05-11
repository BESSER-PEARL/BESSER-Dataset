





import java.util.List;
import java.util.ArrayList;

public class flowchart_Decision  {

    private boolean isDecision;
    private String condition;





    private flowchart_Node flowchart_node;


    public flowchart_Decision(
        boolean isDecision,        String condition    ) {
        this.isDecision = isDecision;
        this.condition = condition;
    }


    public boolean getIsdecision() {
        return isDecision;
    }

    public void setIsdecision(boolean isDecision) {
        this.isDecision = isDecision;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }

    public flowchart_Node getFlowchart_node() {
        return flowchart_node;
    }

    public void setFlowchart_node(flowchart_Node flowchart_node) {
        this.flowchart_node = flowchart_node;
    }

}