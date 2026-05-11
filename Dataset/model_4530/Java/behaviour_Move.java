





import java.util.List;
import java.util.ArrayList;

public class behaviour_Move extends NamedElement {






    private behaviour_Drone behaviour_drone;




    private List<behaviour_Action> behaviour_actions;




    private List<behaviour_Action> behaviour_actions;


    public behaviour_Move(
    ) {
        super(
        );
        this.behaviour_actions = new ArrayList<>();
        this.behaviour_actions = new ArrayList<>();
    }

    public behaviour_Move(
        ArrayList<behaviour_Action> behaviour_actions,        ArrayList<behaviour_Action> behaviour_actions    ) {
        this.behaviour_actions = behaviour_actions;
        this.behaviour_actions = behaviour_actions;
    }


    public behaviour_Drone getBehaviour_drone() {
        return behaviour_drone;
    }

    public void setBehaviour_drone(behaviour_Drone behaviour_drone) {
        this.behaviour_drone = behaviour_drone;
    }
    public List<behaviour_Action> getBehaviour_actions() {
        return behaviour_actions;
    }

    public void addBehaviour_action(Behaviour_action behaviour_action) {
        this.behaviour_actions.add(behaviour_action);
    }
    public List<behaviour_Action> getBehaviour_actions() {
        return behaviour_actions;
    }

    public void addBehaviour_action(Behaviour_action behaviour_action) {
        this.behaviour_actions.add(behaviour_action);
    }

}