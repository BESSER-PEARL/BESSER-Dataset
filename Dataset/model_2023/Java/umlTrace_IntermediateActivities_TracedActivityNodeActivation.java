





import java.util.List;
import java.util.ArrayList;

public class umlTrace_IntermediateActivities_TracedActivityNodeActivation extends TracedSemanticVisitor {






    private List<ActivityNodeActivation_outgoingEdges_Value> activitynodeactivation_outgoingedges_values;




    private List<ActivityNodeActivation_running_Value> activitynodeactivation_running_values;




    private List<ActivityNodeActivation_heldTokens_Value> activitynodeactivation_heldtokens_values;




    private List<ActivityNodeActivation_group_ActivityNodeActivation_Value> activitynodeactivation_group_activitynodeactivation_values;




    private List<ActivityNodeActivation_isRunning_Value> activitynodeactivation_isrunning_values;




    private List<ActivityNodeActivation_incomingEdges_Value> activitynodeactivation_incomingedges_values;




    private List<ActivityNodeActivation_node_ActivityNodeActivation_Value> activitynodeactivation_node_activitynodeactivation_values;


    public umlTrace_IntermediateActivities_TracedActivityNodeActivation(
    ) {
        super(
        );
        this.activitynodeactivation_outgoingedges_values = new ArrayList<>();
        this.activitynodeactivation_running_values = new ArrayList<>();
        this.activitynodeactivation_heldtokens_values = new ArrayList<>();
        this.activitynodeactivation_group_activitynodeactivation_values = new ArrayList<>();
        this.activitynodeactivation_isrunning_values = new ArrayList<>();
        this.activitynodeactivation_incomingedges_values = new ArrayList<>();
        this.activitynodeactivation_node_activitynodeactivation_values = new ArrayList<>();
    }

    public umlTrace_IntermediateActivities_TracedActivityNodeActivation(
        ArrayList<ActivityNodeActivation_outgoingEdges_Value> activitynodeactivation_outgoingedges_values,        ArrayList<ActivityNodeActivation_running_Value> activitynodeactivation_running_values,        ArrayList<ActivityNodeActivation_heldTokens_Value> activitynodeactivation_heldtokens_values,        ArrayList<ActivityNodeActivation_group_ActivityNodeActivation_Value> activitynodeactivation_group_activitynodeactivation_values,        ArrayList<ActivityNodeActivation_isRunning_Value> activitynodeactivation_isrunning_values,        ArrayList<ActivityNodeActivation_incomingEdges_Value> activitynodeactivation_incomingedges_values,        ArrayList<ActivityNodeActivation_node_ActivityNodeActivation_Value> activitynodeactivation_node_activitynodeactivation_values    ) {
        this.activitynodeactivation_outgoingedges_values = activitynodeactivation_outgoingedges_values;
        this.activitynodeactivation_running_values = activitynodeactivation_running_values;
        this.activitynodeactivation_heldtokens_values = activitynodeactivation_heldtokens_values;
        this.activitynodeactivation_group_activitynodeactivation_values = activitynodeactivation_group_activitynodeactivation_values;
        this.activitynodeactivation_isrunning_values = activitynodeactivation_isrunning_values;
        this.activitynodeactivation_incomingedges_values = activitynodeactivation_incomingedges_values;
        this.activitynodeactivation_node_activitynodeactivation_values = activitynodeactivation_node_activitynodeactivation_values;
    }


    public List<ActivityNodeActivation_outgoingEdges_Value> getActivitynodeactivation_outgoingedges_values() {
        return activitynodeactivation_outgoingedges_values;
    }

    public void addActivitynodeactivation_outgoingedges_value(Activitynodeactivation_outgoingedges_value activitynodeactivation_outgoingedges_value) {
        this.activitynodeactivation_outgoingedges_values.add(activitynodeactivation_outgoingedges_value);
    }
    public List<ActivityNodeActivation_running_Value> getActivitynodeactivation_running_values() {
        return activitynodeactivation_running_values;
    }

    public void addActivitynodeactivation_running_value(Activitynodeactivation_running_value activitynodeactivation_running_value) {
        this.activitynodeactivation_running_values.add(activitynodeactivation_running_value);
    }
    public List<ActivityNodeActivation_heldTokens_Value> getActivitynodeactivation_heldtokens_values() {
        return activitynodeactivation_heldtokens_values;
    }

    public void addActivitynodeactivation_heldtokens_value(Activitynodeactivation_heldtokens_value activitynodeactivation_heldtokens_value) {
        this.activitynodeactivation_heldtokens_values.add(activitynodeactivation_heldtokens_value);
    }
    public List<ActivityNodeActivation_group_ActivityNodeActivation_Value> getActivitynodeactivation_group_activitynodeactivation_values() {
        return activitynodeactivation_group_activitynodeactivation_values;
    }

    public void addActivitynodeactivation_group_activitynodeactivation_value(Activitynodeactivation_group_activitynodeactivation_value activitynodeactivation_group_activitynodeactivation_value) {
        this.activitynodeactivation_group_activitynodeactivation_values.add(activitynodeactivation_group_activitynodeactivation_value);
    }
    public List<ActivityNodeActivation_isRunning_Value> getActivitynodeactivation_isrunning_values() {
        return activitynodeactivation_isrunning_values;
    }

    public void addActivitynodeactivation_isrunning_value(Activitynodeactivation_isrunning_value activitynodeactivation_isrunning_value) {
        this.activitynodeactivation_isrunning_values.add(activitynodeactivation_isrunning_value);
    }
    public List<ActivityNodeActivation_incomingEdges_Value> getActivitynodeactivation_incomingedges_values() {
        return activitynodeactivation_incomingedges_values;
    }

    public void addActivitynodeactivation_incomingedges_value(Activitynodeactivation_incomingedges_value activitynodeactivation_incomingedges_value) {
        this.activitynodeactivation_incomingedges_values.add(activitynodeactivation_incomingedges_value);
    }
    public List<ActivityNodeActivation_node_ActivityNodeActivation_Value> getActivitynodeactivation_node_activitynodeactivation_values() {
        return activitynodeactivation_node_activitynodeactivation_values;
    }

    public void addActivitynodeactivation_node_activitynodeactivation_value(Activitynodeactivation_node_activitynodeactivation_value activitynodeactivation_node_activitynodeactivation_value) {
        this.activitynodeactivation_node_activitynodeactivation_values.add(activitynodeactivation_node_activitynodeactivation_value);
    }

}