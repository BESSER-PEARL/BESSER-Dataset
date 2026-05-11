





import java.util.List;
import java.util.ArrayList;

public class umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup  {






    private List<ActivityNodeActivationGroup_nodeActivations_Value> activitynodeactivationgroup_nodeactivations_values;




    private List<ActivityNodeActivationGroup_activityExecution_Value> activitynodeactivationgroup_activityexecution_values;




    private List<ActivityNodeActivationGroup_edgeInstances_Value> activitynodeactivationgroup_edgeinstances_values;


    public umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup(
    ) {
        this.activitynodeactivationgroup_nodeactivations_values = new ArrayList<>();
        this.activitynodeactivationgroup_activityexecution_values = new ArrayList<>();
        this.activitynodeactivationgroup_edgeinstances_values = new ArrayList<>();
    }

    public umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup(
        ArrayList<ActivityNodeActivationGroup_nodeActivations_Value> activitynodeactivationgroup_nodeactivations_values,        ArrayList<ActivityNodeActivationGroup_activityExecution_Value> activitynodeactivationgroup_activityexecution_values,        ArrayList<ActivityNodeActivationGroup_edgeInstances_Value> activitynodeactivationgroup_edgeinstances_values    ) {
        this.activitynodeactivationgroup_nodeactivations_values = activitynodeactivationgroup_nodeactivations_values;
        this.activitynodeactivationgroup_activityexecution_values = activitynodeactivationgroup_activityexecution_values;
        this.activitynodeactivationgroup_edgeinstances_values = activitynodeactivationgroup_edgeinstances_values;
    }


    public List<ActivityNodeActivationGroup_nodeActivations_Value> getActivitynodeactivationgroup_nodeactivations_values() {
        return activitynodeactivationgroup_nodeactivations_values;
    }

    public void addActivitynodeactivationgroup_nodeactivations_value(Activitynodeactivationgroup_nodeactivations_value activitynodeactivationgroup_nodeactivations_value) {
        this.activitynodeactivationgroup_nodeactivations_values.add(activitynodeactivationgroup_nodeactivations_value);
    }
    public List<ActivityNodeActivationGroup_activityExecution_Value> getActivitynodeactivationgroup_activityexecution_values() {
        return activitynodeactivationgroup_activityexecution_values;
    }

    public void addActivitynodeactivationgroup_activityexecution_value(Activitynodeactivationgroup_activityexecution_value activitynodeactivationgroup_activityexecution_value) {
        this.activitynodeactivationgroup_activityexecution_values.add(activitynodeactivationgroup_activityexecution_value);
    }
    public List<ActivityNodeActivationGroup_edgeInstances_Value> getActivitynodeactivationgroup_edgeinstances_values() {
        return activitynodeactivationgroup_edgeinstances_values;
    }

    public void addActivitynodeactivationgroup_edgeinstances_value(Activitynodeactivationgroup_edgeinstances_value activitynodeactivationgroup_edgeinstances_value) {
        this.activitynodeactivationgroup_edgeinstances_values.add(activitynodeactivationgroup_edgeinstances_value);
    }

}