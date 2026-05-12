





import java.util.List;
import java.util.ArrayList;

public class statechart_Node  {

    private String activity;
    private String type;
    private String label;
    private String name;





    private statechart_Node statechart_node;




    private statechart_Model statechart_model;




    private statechart_Node statechart_node;


    public statechart_Node(
        String activity,        String type,        String label,        String name    ) {
        this.activity = activity;
        this.type = type;
        this.label = label;
        this.name = name;
    }


    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public statechart_Node getStatechart_node() {
        return statechart_node;
    }

    public void setStatechart_node(statechart_Node statechart_node) {
        this.statechart_node = statechart_node;
    }

}