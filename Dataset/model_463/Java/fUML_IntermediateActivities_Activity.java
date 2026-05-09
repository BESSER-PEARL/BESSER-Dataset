





import java.util.List;
import java.util.ArrayList;

public class fUML_IntermediateActivities_Activity extends Behavior {

    private boolean readOnly;





    private List<IntermediateActivities_ActivityNode> intermediateactivities_activitynodes;


    public fUML_IntermediateActivities_Activity(
        boolean readOnly    ) {
        super(
        );
        this.readOnly = readOnly;
        this.intermediateactivities_activitynodes = new ArrayList<>();
    }

    public fUML_IntermediateActivities_Activity(
        boolean readOnly        ArrayList<IntermediateActivities_ActivityNode> intermediateactivities_activitynodes    ) {
        this.readOnly = readOnly;
        this.intermediateactivities_activitynodes = intermediateactivities_activitynodes;
    }

    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }

    public List<IntermediateActivities_ActivityNode> getIntermediateactivities_activitynodes() {
        return intermediateactivities_activitynodes;
    }

    public void addIntermediateactivities_activitynode(Intermediateactivities_activitynode intermediateactivities_activitynode) {
        this.intermediateactivities_activitynodes.add(intermediateactivities_activitynode);
    }

}