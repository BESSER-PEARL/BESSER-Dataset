





import java.util.List;
import java.util.ArrayList;

public class umlTrace_IntermediateActivities_TracedActivityExecution extends TracedExecution {






    private List<ActivityExecution_activationGroup_Value> activityexecution_activationgroup_values;


    public umlTrace_IntermediateActivities_TracedActivityExecution(
    ) {
        super(
        );
        this.activityexecution_activationgroup_values = new ArrayList<>();
    }

    public umlTrace_IntermediateActivities_TracedActivityExecution(
        ArrayList<ActivityExecution_activationGroup_Value> activityexecution_activationgroup_values    ) {
        this.activityexecution_activationgroup_values = activityexecution_activationgroup_values;
    }


    public List<ActivityExecution_activationGroup_Value> getActivityexecution_activationgroup_values() {
        return activityexecution_activationgroup_values;
    }

    public void addActivityexecution_activationgroup_value(Activityexecution_activationgroup_value activityexecution_activationgroup_value) {
        this.activityexecution_activationgroup_values.add(activityexecution_activationgroup_value);
    }

}