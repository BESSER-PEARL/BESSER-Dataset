





import java.util.List;
import java.util.ArrayList;

public class flowchart_Action  {

    private boolean isAction;





    private flowchart_Node flowchart_node;


    public flowchart_Action(
        boolean isAction    ) {
        this.isAction = isAction;
    }


    public boolean getIsaction() {
        return isAction;
    }

    public void setIsaction(boolean isAction) {
        this.isAction = isAction;
    }

    public flowchart_Node getFlowchart_node() {
        return flowchart_node;
    }

    public void setFlowchart_node(flowchart_Node flowchart_node) {
        this.flowchart_node = flowchart_node;
    }

}