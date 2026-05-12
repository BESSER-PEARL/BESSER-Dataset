





import java.util.List;
import java.util.ArrayList;

public class statechart_Variable  {

    private String name;
    private String type;





    private statechart_Node statechart_node;




    private statechart_Model statechart_model;


    public statechart_Variable(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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