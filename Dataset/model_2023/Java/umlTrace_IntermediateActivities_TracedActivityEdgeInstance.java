





import java.util.List;
import java.util.ArrayList;

public class umlTrace_IntermediateActivities_TracedActivityEdgeInstance  {






    private List<ActivityEdgeInstance_offers_Value> activityedgeinstance_offers_values;




    private List<ActivityEdgeInstance_edge_ActivityEdgeInstance_Value> activityedgeinstance_edge_activityedgeinstance_values;




    private List<ActivityEdgeInstance_target_Value> activityedgeinstance_target_values;




    private List<ActivityEdgeInstance_group_ActivityEdgeInstance_Value> activityedgeinstance_group_activityedgeinstance_values;




    private List<ActivityEdgeInstance_source_Value> activityedgeinstance_source_values;


    public umlTrace_IntermediateActivities_TracedActivityEdgeInstance(
    ) {
        this.activityedgeinstance_offers_values = new ArrayList<>();
        this.activityedgeinstance_edge_activityedgeinstance_values = new ArrayList<>();
        this.activityedgeinstance_target_values = new ArrayList<>();
        this.activityedgeinstance_group_activityedgeinstance_values = new ArrayList<>();
        this.activityedgeinstance_source_values = new ArrayList<>();
    }

    public umlTrace_IntermediateActivities_TracedActivityEdgeInstance(
        ArrayList<ActivityEdgeInstance_offers_Value> activityedgeinstance_offers_values,        ArrayList<ActivityEdgeInstance_edge_ActivityEdgeInstance_Value> activityedgeinstance_edge_activityedgeinstance_values,        ArrayList<ActivityEdgeInstance_target_Value> activityedgeinstance_target_values,        ArrayList<ActivityEdgeInstance_group_ActivityEdgeInstance_Value> activityedgeinstance_group_activityedgeinstance_values,        ArrayList<ActivityEdgeInstance_source_Value> activityedgeinstance_source_values    ) {
        this.activityedgeinstance_offers_values = activityedgeinstance_offers_values;
        this.activityedgeinstance_edge_activityedgeinstance_values = activityedgeinstance_edge_activityedgeinstance_values;
        this.activityedgeinstance_target_values = activityedgeinstance_target_values;
        this.activityedgeinstance_group_activityedgeinstance_values = activityedgeinstance_group_activityedgeinstance_values;
        this.activityedgeinstance_source_values = activityedgeinstance_source_values;
    }


    public List<ActivityEdgeInstance_offers_Value> getActivityedgeinstance_offers_values() {
        return activityedgeinstance_offers_values;
    }

    public void addActivityedgeinstance_offers_value(Activityedgeinstance_offers_value activityedgeinstance_offers_value) {
        this.activityedgeinstance_offers_values.add(activityedgeinstance_offers_value);
    }
    public List<ActivityEdgeInstance_edge_ActivityEdgeInstance_Value> getActivityedgeinstance_edge_activityedgeinstance_values() {
        return activityedgeinstance_edge_activityedgeinstance_values;
    }

    public void addActivityedgeinstance_edge_activityedgeinstance_value(Activityedgeinstance_edge_activityedgeinstance_value activityedgeinstance_edge_activityedgeinstance_value) {
        this.activityedgeinstance_edge_activityedgeinstance_values.add(activityedgeinstance_edge_activityedgeinstance_value);
    }
    public List<ActivityEdgeInstance_target_Value> getActivityedgeinstance_target_values() {
        return activityedgeinstance_target_values;
    }

    public void addActivityedgeinstance_target_value(Activityedgeinstance_target_value activityedgeinstance_target_value) {
        this.activityedgeinstance_target_values.add(activityedgeinstance_target_value);
    }
    public List<ActivityEdgeInstance_group_ActivityEdgeInstance_Value> getActivityedgeinstance_group_activityedgeinstance_values() {
        return activityedgeinstance_group_activityedgeinstance_values;
    }

    public void addActivityedgeinstance_group_activityedgeinstance_value(Activityedgeinstance_group_activityedgeinstance_value activityedgeinstance_group_activityedgeinstance_value) {
        this.activityedgeinstance_group_activityedgeinstance_values.add(activityedgeinstance_group_activityedgeinstance_value);
    }
    public List<ActivityEdgeInstance_source_Value> getActivityedgeinstance_source_values() {
        return activityedgeinstance_source_values;
    }

    public void addActivityedgeinstance_source_value(Activityedgeinstance_source_value activityedgeinstance_source_value) {
        this.activityedgeinstance_source_values.add(activityedgeinstance_source_value);
    }

}