





import java.util.List;
import java.util.ArrayList;

public class Behaviour_Connection extends Identifier {






    private Behaviour_Transition behaviour_transition;




    private Behaviour_Description behaviour_description;




    private Behaviour_Place behaviour_place;


    public Behaviour_Connection(
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
    public Behaviour_Description getBehaviour_description() {
        return behaviour_description;
    }

    public void setBehaviour_description(Behaviour_Description behaviour_description) {
        this.behaviour_description = behaviour_description;
    }
    public Behaviour_Place getBehaviour_place() {
        return behaviour_place;
    }

    public void setBehaviour_place(Behaviour_Place behaviour_place) {
        this.behaviour_place = behaviour_place;
    }

}