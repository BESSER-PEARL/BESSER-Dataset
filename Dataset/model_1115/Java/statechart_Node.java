





import java.util.List;
import java.util.ArrayList;

public class statechart_Node  {

    private String type;
    private String activity;
    private String actions;
    private String name;
    private String label;
    private String metadata;





    private List<statechart_Node> statechart_nodes;




    private statechart_Node statechart_node;




    private statechart_Model statechart_model;


    public statechart_Node(
        String type,        String activity,        String actions,        String name,        String label,        String metadata    ) {
        this.type = type;
        this.activity = activity;
        this.actions = actions;
        this.name = name;
        this.label = label;
        this.metadata = metadata;
        this.statechart_nodes = new ArrayList<>();
    }

    public statechart_Node(
        String type,        String activity,        String actions,        String name,        String label,        String metadata        ArrayList<statechart_Node> statechart_nodes    ) {
        this.type = type;
        this.activity = activity;
        this.actions = actions;
        this.name = name;
        this.label = label;
        this.metadata = metadata;
        this.statechart_nodes = statechart_nodes;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public String getActions() {
        return actions;
    }

    public void setActions(String actions) {
        this.actions = actions;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getMetadata() {
        return metadata;
    }

    public void setMetadata(String metadata) {
        this.metadata = metadata;
    }

    public List<statechart_Node> getStatechart_nodes() {
        return statechart_nodes;
    }

    public void addStatechart_node(Statechart_node statechart_node) {
        this.statechart_nodes.add(statechart_node);
    }
    public statechart_Node getStatechart_node() {
        return statechart_node;
    }

    public void setStatechart_node(statechart_Node statechart_node) {
        this.statechart_node = statechart_node;
    }
    public statechart_Model getStatechart_model() {
        return statechart_model;
    }

    public void setStatechart_model(statechart_Model statechart_model) {
        this.statechart_model = statechart_model;
    }

}