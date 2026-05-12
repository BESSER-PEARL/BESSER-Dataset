





import java.util.List;
import java.util.ArrayList;

public class statechart_Transition  {

    private String TE;
    private String name;





    private statechart_Node statechart_node;




    private statechart_Node statechart_node;




    private statechart_Model statechart_model;


    public statechart_Transition(
        String TE,        String name    ) {
        this.TE = TE;
        this.name = name;
    }


    public String getTe() {
        return TE;
    }

    public void setTe(String TE) {
        this.TE = TE;
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