





import java.util.List;
import java.util.ArrayList;

public class Behaviour_PreTransitionConnection extends Connection {

    private int requiredTokenAmount;





    private Behaviour_Transition behaviour_transition;


    public Behaviour_PreTransitionConnection(
        int requiredTokenAmount    ) {
        super(
        );
        this.requiredTokenAmount = requiredTokenAmount;
    }


    public int getRequiredtokenamount() {
        return requiredTokenAmount;
    }

    public void setRequiredtokenamount(int requiredTokenAmount) {
        this.requiredTokenAmount = requiredTokenAmount;
    }

    public Behaviour_Transition getBehaviour_transition() {
        return behaviour_transition;
    }

    public void setBehaviour_transition(Behaviour_Transition behaviour_transition) {
        this.behaviour_transition = behaviour_transition;
    }

}