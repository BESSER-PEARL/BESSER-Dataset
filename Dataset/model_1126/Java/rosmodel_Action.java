





import java.util.List;
import java.util.ArrayList;

public class rosmodel_Action  {

    private String name;





    private rosmodel_Transition rosmodel_transition;




    private rosmodel_Transition rosmodel_transition;




    private rosmodel_Node rosmodel_node;


    public rosmodel_Action(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rosmodel_Transition getRosmodel_transition() {
        return rosmodel_transition;
    }

    public void setRosmodel_transition(rosmodel_Transition rosmodel_transition) {
        this.rosmodel_transition = rosmodel_transition;
    }
    public rosmodel_Transition getRosmodel_transition() {
        return rosmodel_transition;
    }

    public void setRosmodel_transition(rosmodel_Transition rosmodel_transition) {
        this.rosmodel_transition = rosmodel_transition;
    }
    public rosmodel_Node getRosmodel_node() {
        return rosmodel_node;
    }

    public void setRosmodel_node(rosmodel_Node rosmodel_node) {
        this.rosmodel_node = rosmodel_node;
    }

}