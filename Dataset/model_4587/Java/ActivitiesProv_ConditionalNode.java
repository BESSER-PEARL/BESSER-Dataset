





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_ConditionalNode extends StructuredActivityNode {

    private boolean isDeterminate;
    private boolean isAssumed;





    private List<ActivitiesProv_ExecutableNode> activitiesprov_executablenodes;




    private List<ActivitiesProv_ExecutableNode> activitiesprov_executablenodes;


    public ActivitiesProv_ConditionalNode(
        boolean isDeterminate,        boolean isAssumed    ) {
        super(
        );
        this.isDeterminate = isDeterminate;
        this.isAssumed = isAssumed;
        this.activitiesprov_executablenodes = new ArrayList<>();
        this.activitiesprov_executablenodes = new ArrayList<>();
    }

    public ActivitiesProv_ConditionalNode(
        boolean isDeterminate,        boolean isAssumed        ArrayList<ActivitiesProv_ExecutableNode> activitiesprov_executablenodes,        ArrayList<ActivitiesProv_ExecutableNode> activitiesprov_executablenodes    ) {
        this.isDeterminate = isDeterminate;
        this.isAssumed = isAssumed;
        this.activitiesprov_executablenodes = activitiesprov_executablenodes;
        this.activitiesprov_executablenodes = activitiesprov_executablenodes;
    }

    public boolean getIsdeterminate() {
        return isDeterminate;
    }

    public void setIsdeterminate(boolean isDeterminate) {
        this.isDeterminate = isDeterminate;
    }
    public boolean getIsassumed() {
        return isAssumed;
    }

    public void setIsassumed(boolean isAssumed) {
        this.isAssumed = isAssumed;
    }

    public List<ActivitiesProv_ExecutableNode> getActivitiesprov_executablenodes() {
        return activitiesprov_executablenodes;
    }

    public void addActivitiesprov_executablenode(Activitiesprov_executablenode activitiesprov_executablenode) {
        this.activitiesprov_executablenodes.add(activitiesprov_executablenode);
    }
    public List<ActivitiesProv_ExecutableNode> getActivitiesprov_executablenodes() {
        return activitiesprov_executablenodes;
    }

    public void addActivitiesprov_executablenode(Activitiesprov_executablenode activitiesprov_executablenode) {
        this.activitiesprov_executablenodes.add(activitiesprov_executablenode);
    }

}