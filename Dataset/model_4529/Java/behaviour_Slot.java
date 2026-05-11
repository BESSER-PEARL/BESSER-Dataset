





import java.util.List;
import java.util.ArrayList;

public class behaviour_Slot extends NamedElement {






    private behaviour_Drone behaviour_drone;




    private behaviour_MoveTransition behaviour_movetransition;


    public behaviour_Slot(
    ) {
        super(
        );
    }



    public behaviour_Drone getBehaviour_drone() {
        return behaviour_drone;
    }

    public void setBehaviour_drone(behaviour_Drone behaviour_drone) {
        this.behaviour_drone = behaviour_drone;
    }
    public behaviour_MoveTransition getBehaviour_movetransition() {
        return behaviour_movetransition;
    }

    public void setBehaviour_movetransition(behaviour_MoveTransition behaviour_movetransition) {
        this.behaviour_movetransition = behaviour_movetransition;
    }

}