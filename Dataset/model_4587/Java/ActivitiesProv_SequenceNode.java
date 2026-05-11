





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_SequenceNode extends StructuredActivityNode {






    private List<ActivitiesProv_ExecutableNode> activitiesprov_executablenodes;


    public ActivitiesProv_SequenceNode(
    ) {
        super(
        );
        this.activitiesprov_executablenodes = new ArrayList<>();
    }

    public ActivitiesProv_SequenceNode(
        ArrayList<ActivitiesProv_ExecutableNode> activitiesprov_executablenodes    ) {
        this.activitiesprov_executablenodes = activitiesprov_executablenodes;
    }


    public List<ActivitiesProv_ExecutableNode> getActivitiesprov_executablenodes() {
        return activitiesprov_executablenodes;
    }

    public void addActivitiesprov_executablenode(Activitiesprov_executablenode activitiesprov_executablenode) {
        this.activitiesprov_executablenodes.add(activitiesprov_executablenode);
    }

}