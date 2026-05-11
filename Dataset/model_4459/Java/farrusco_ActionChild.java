





import java.util.List;
import java.util.ArrayList;

public class farrusco_ActionChild  {






    private farrusco_Behavior farrusco_behavior;




    private farrusco_Robot farrusco_robot;




    private List<farrusco_Action> farrusco_actions;


    public farrusco_ActionChild(
    ) {
        this.farrusco_actions = new ArrayList<>();
    }

    public farrusco_ActionChild(
        ArrayList<farrusco_Action> farrusco_actions    ) {
        this.farrusco_actions = farrusco_actions;
    }


    public farrusco_Behavior getFarrusco_behavior() {
        return farrusco_behavior;
    }

    public void setFarrusco_behavior(farrusco_Behavior farrusco_behavior) {
        this.farrusco_behavior = farrusco_behavior;
    }
    public farrusco_Robot getFarrusco_robot() {
        return farrusco_robot;
    }

    public void setFarrusco_robot(farrusco_Robot farrusco_robot) {
        this.farrusco_robot = farrusco_robot;
    }
    public List<farrusco_Action> getFarrusco_actions() {
        return farrusco_actions;
    }

    public void addFarrusco_action(Farrusco_action farrusco_action) {
        this.farrusco_actions.add(farrusco_action);
    }

}