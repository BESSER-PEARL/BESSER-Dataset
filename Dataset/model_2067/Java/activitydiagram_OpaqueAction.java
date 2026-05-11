





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_OpaqueAction extends Action {






    private List<activitydiagram_VariableAssignment> activitydiagram_variableassignments;


    public activitydiagram_OpaqueAction(
    ) {
        super(
        );
        this.activitydiagram_variableassignments = new ArrayList<>();
    }

    public activitydiagram_OpaqueAction(
        ArrayList<activitydiagram_VariableAssignment> activitydiagram_variableassignments    ) {
        this.activitydiagram_variableassignments = activitydiagram_variableassignments;
    }


    public List<activitydiagram_VariableAssignment> getActivitydiagram_variableassignments() {
        return activitydiagram_variableassignments;
    }

    public void addActivitydiagram_variableassignment(Activitydiagram_variableassignment activitydiagram_variableassignment) {
        this.activitydiagram_variableassignments.add(activitydiagram_variableassignment);
    }

}