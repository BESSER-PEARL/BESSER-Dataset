





import java.util.List;
import java.util.ArrayList;

public class Behaviour_PostTransitionConnection extends Connection {






    private Behaviour_Transition behaviour_transition;


    public Behaviour_PostTransitionConnection(
    ) {
        super(
        );
    }



    public Behaviour_Transition getBehaviour_transition() {
        return behaviour_transition;
    }

    public void setBehaviour_transition(Behaviour_Transition behaviour_transition) {
        this.behaviour_transition = behaviour_transition;
    }

}